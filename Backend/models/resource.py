from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Resource(db.Model):
    __tablename__ = 'publicar_aviso'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    sede = db.Column(db.String(100), nullable=False)
    item_image = db.Column(db.String(255), nullable=True)
    item_description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'contact_number': self.contact_number,
            'sede': self.sede,
            'item_image': self.item_image,
            'item_description': self.item_description
        }
