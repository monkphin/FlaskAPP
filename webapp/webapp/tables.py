from flask_table import Table, Col, LinkCol

class Credentials(Table):
    credId = Col('credId', show=False)
    username = Col('username')
    userpwd = Col('userpwd', show=False)

class Persons(Table):
    PersonID = Col('PersonID', show=False)
    LastName = Col('LastName')
    FirstName = Col('FirstName')
    email = Col('email')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='Personid'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='Personid'))


class Game_System(Table):
    SystemID = Col('SystemID', show=False)
    Company = Col('Company')
    Game_System = Col('Game_System')
    Project_Name = Col('Project_Name')

class Mini_Collection(Table):
    MiniID = Col('MiniID', show=False)
    MiniName = Col('MiniName')
    MiniType = Col('MiniType')
    MiniNum = Col('MiniNum')
    MiniPoint = Col('MiniPoint')
    MiniCost = Col('MiniCost')
