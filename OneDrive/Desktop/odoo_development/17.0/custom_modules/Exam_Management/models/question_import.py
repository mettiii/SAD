from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64
import csv
import io
import logging

_logger = logging.getLogger(__name__)


class ExamQuestionImportWizard(models.Model):
    _name = 'exam.question.import.wizard'
    _description = 'Import Exam Questions Wizard'

    upload_file = fields.Binary(string="Upload CSV File", required=True)
    upload_filename = fields.Char(string="Filename")
    name = fields.Char(string="Exam Title")

    question_ids = fields.One2many(
        'exam.question',
        'import_wizard_id',
        string="Imported Questions",
        readonly=True,
    )

    exam_file_ids = fields.One2many(
        'exam.management.file',
        'question_id',
        string="Upload Question Files"
    )

    def action_import_questions(self):
        imported_questions = []
        row_num = 1
        if self.exam_file_ids:
            for exam_file in self.exam_file_ids:
                try:
                    file_content = base64.b64decode(exam_file.file_data)
                    file_str = io.StringIO(file_content.decode("utf-8"))
                    reader = csv.reader(file_str)
                except Exception as e:
                    raise ValidationError(f"Failed to read CSV file: {e}")

                headers = next(reader, None)
                _logger.warning(f"CSV HEADER: {headers} (length: {len(headers) if headers else 0})")
                if not headers or len(headers) < 12:
                    raise ValidationError("Invalid or missing CSV header. Expected at least 12 columns.")

                for row in reader:
                    row_num += 1
                    if not row or not row[0].strip() or not row[1].strip():
                        _logger.info(f"Row {row_num} skipped: missing question text or type. Row: {row}")
                        continue
                    if len(row) < 12:
                        row += [''] * (12 - len(row))
                    question_text = row[0].strip()
                    question_type = row[1].strip().lower()
                    exam_type = row[7].strip().lower()
                    job_grade = row[8].strip().lower()
                    job_role = row[9].strip().lower()
                    department_id = row[10].strip().lower()
                    mark = float(row[15].strip()) if len(row) > 15 and row[15].strip() else 1.0
                    question_data = {
                        'name': question_text,
                        'question_type': question_type,
                        'exam_type': exam_type,
                        'job_grade': job_grade,
                        'job_role': job_role,
                        'department_id': department_id,
                        'mark': mark,
                        'import_wizard_id': self.id,
                    }
                    if question_type == 'multiple_choice':
                        question_data.update({
                            'option_a': row[2].strip(),
                            'option_b': row[3].strip(),
                            'option_c': row[4].strip(),
                            'option_d': row[5].strip(),
                            'correct_ans': row[6].strip(),
                        })
                    elif question_type == 'true_false':
                        question_data['correct_ans'] = row[6].strip()
                    elif question_type == 'essay':
                        question_data['correct_ans'] = row[6].strip()
                    else:
                        _logger.info(f"Row {row_num} skipped: unsupported question type '{question_type}'. Row: {row}")
                        continue
                    try:
                        question = self.env['exam.question'].create(question_data)
                        imported_questions.append(question.id)
                        _logger.info(f"Row {row_num} imported: {question_data}")
                    except Exception as e:
                        _logger.error(f"Error importing question at row {row_num}: {row[0]} | Details: {str(e)}")
                        continue
        else:
            # fallback to single file upload if present
            if not self.upload_file:
                raise ValidationError("Please upload a CSV file.")
            try:
                file_content = base64.b64decode(self.upload_file)
                file_str = io.StringIO(file_content.decode("utf-8"))
                reader = csv.reader(file_str)
            except Exception as e:
                raise ValidationError(f"Failed to read CSV file: {e}")
            # headers = next(reader, None)
            # _logger.warning(f"CSV HEADER: {headers} (length: {len(headers) if headers else 0})")
            # if not headers or len(headers) < 12:
            #     raise ValidationError("Invalid or missing CSV header. Expected at least 12 columns.")
            for row in reader:
                row_num += 1
                if not row or not row[0].strip() or not row[1].strip():
                    _logger.info(f"Row {row_num} skipped: missing question text or type. Row: {row}")
                    continue
                if len(row) < 12:
                    row += [''] * (12 - len(row))
                question_text = row[0].strip()
                question_type = row[1].strip().lower()
                exam_type = row[7].strip().lower()
                job_grade = row[8].strip().lower()
                job_role = row[9].strip().lower()
                department_id = row[10].strip().lower()
                mark = float(row[15].strip()) if len(row) > 15 and row[15].strip() else 1.0
                question_data = {
                    'name': question_text,
                    'question_type': question_type,
                    'exam_type': exam_type,
                    'job_grade': job_grade,
                    'job_role': job_role,
                    'department_id': department_id,
                    'mark': mark,
                    'import_wizard_id': self.id,
                }
                if question_type == 'multiple_choice':
                    question_data.update({
                        'option_a': row[2].strip(),
                        'option_b': row[3].strip(),
                        'option_c': row[4].strip(),
                        'option_d': row[5].strip(),
                        'correct_ans': row[6].strip(),
                    })
                elif question_type == 'true_false':
                    question_data['correct_ans'] = row[6].strip()
                elif question_type == 'essay':
                    question_data['correct_ans'] = row[6].strip()
                else:
                    _logger.info(f"Row {row_num} skipped: unsupported question type '{question_type}'. Row: {row}")
                    continue
                try:
                    question = self.env['exam.question'].create(question_data)
                    imported_questions.append(question.id)
                    _logger.info(f"Row {row_num} imported: {question_data}")
                except Exception as e:
                    _logger.error(f"Error importing question at row {row_num}: {row[0]} | Details: {str(e)}")
                    continue
        if not imported_questions:
            raise ValidationError(
                "No questions were imported. Please check your CSV format and values. Check the server logs for details.")
        self.question_ids = [(6, 0, imported_questions)]
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
