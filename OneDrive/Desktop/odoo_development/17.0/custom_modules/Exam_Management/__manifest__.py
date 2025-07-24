{
    'name': 'Bunna Bank Exam Management System',
    'author': 'Internship Projects',
    'sequence': -500,
    'license': 'LGPL-3',
    'version': '1.0',
    'depends': [
        'base',
        'mail',
        'hr'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/template.xml',
        # 'security/exam_security.xml',
        'views/exam_question_views.xml',
        'views/exam_views.xml',
        'views/employee.xml',
        'views/exam_list.xml',
        'views/exam_result_views.xml',
        # 'views/question_display.xml',
        'views/view_question_import.xml',  # keep only one occurrence
        'views/exam_menu_views.xml',
        'report/scorecard_report.xml',
        'views/exam_login_template.xml',
        'views/exam_dashboard_template.xml',
        'views/exam_paper_template.xml'
        # 'views/template.xml'
    ],

    'asset': {
        'web.backend': [
            'static\src\js\exam_protection.js',
        ]
    },
    'installable': True,
    'application': True,
}
