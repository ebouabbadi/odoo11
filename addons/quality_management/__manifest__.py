{
    'name': 'Quality Management',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Module to manage product quality checks',
    'description': """
Quality Management
===================
This module allows you to manage quality checks and inspections for your products.
""",
    'author': 'Mehdi Bouabbadi',
    'depends': ['base', 'stock'],  # Add dependencies like `stock` if you want to manage inventory-related quality checks
    'data': [
        'views/quality_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
