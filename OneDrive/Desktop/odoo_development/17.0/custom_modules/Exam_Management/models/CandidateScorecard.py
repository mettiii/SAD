from odoo import models, fields, api

class CandidateScorecard(models.Model):
    _name = "candidate.scorecard"
    _description = "Candidate Scorecard"

    candidate_id = fields.Many2one('hr.employee', string="Candidate", required=True)
    exam_id = fields.Many2one('exam.management', string="Exam", required=True)
    score = fields.Float(string="Score", required=True)
    feedback = fields.Text(string="Feedback")

    @api.model
    def create_scorecard(self, candidate_id, exam_id, score, feedback):
        """Create a scorecard for a candidate."""
        scorecard = self.create({
            'candidate_id': candidate_id,
            'exam_id': exam_id,
            'score': score,
            'feedback': feedback,
        })
        return scorecard