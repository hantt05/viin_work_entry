from odoo.tests import tagged
from odoo.exceptions import AccessError

@classmethod
def setUpClass(cls):
    super().setUpClass()
    # Create user.
    cls.env.user_demo = cls.env.ref('base.user_demo')
    # User has group 'group_hr_user'
    cls.partner_a = cls.env['res.partner'].with_context(tracking_disable=True).create({
        'name': 'partner_a',
        'company_id': False
    })
    #create new employee
    cls.employee = cls.env['hr.employee'].with_context(tracking_disable=True).create({
        'name': 'Employee',
        'address_home_id': cls.partner_a.id
        })

class Test(ViinWorkEntry):
    def test_hr_user(self):
        
        
        pass
    
    
    def test_hr_superuser(self):
        pass
    
    def test_hr_admin(self):
        pass