__author__ = 'cheon'

from app import db


class Location(db.Model):
    __bind_key__ = 'innobid'
    __tablename__ = 'os_t_city'
    pk_i_id = db.Column(db.Integer, primary_key=True)
    fk_i_region_id = db.Column(db.Integer)
    s_name = db.Column(db.String(60))
    s_slug = db.Column(db.String(60))


class License(db.Model):
    __bind_key__ = 'innobid'
    __tablename__ = 'os_t_category_description'
    fk_i_category_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(100))
    s_description = db.Column(db.String(100))
    s_slug = db.Column(db.String(4))


licenses = db.Table('os_t_item_bids_attr_license',
                    db.Column('item_id', db.Integer, db.ForeignKey('os_t_item.pk_i_id')),
                    db.Column('license_id', db.Integer, db.ForeignKey('os_t_category_description.fk_i_category_id')),
                    info={'bind_key': 'innobid'}
            )

locations = db.Table('os_t_item_bids_attr_location',
                     db.Column('item_id', db.Integer, db.ForeignKey('os_t_item.pk_i_id')),
                     db.Column('location_id', db.Integer, db.ForeignKey('os_t_city.pk_i_id')),
                     info={'bind_key':'innobid'}
            )

class Bid(db.Model):
    __tablename__ = 'os_t_item'
    __bind_key__ = 'innobid'
    pk_i_id = db.Column('pk_i_id', db.Integer, primary_key=True)
    dt_mod_date = db.Column('dt_mod_date', db.DateTime)
    i_price = db.Column('i_price', db.BigInteger)
    s_url = db.Column('s_url', db.String(150))
    attr = db.relationship('BidsAttr', backref='bid', uselist=False, lazy='joined')
    licenses = db.relationship('License', secondary=licenses)
    locations = db.relationship('Location', secondary=locations)


class BidsAttr(db.Model):
    __tablename__ = 'os_t_item_bids_attr'
    __bind_key__ = 'innobid'
    fk_i_item_id = db.Column('fk_i_item_id', db.Integer, db.ForeignKey('os_t_item.pk_i_id'), primary_key=True)
    NoticeNumber = db.Column('s_NoticeNumber', db.String(40))
    NoticeName = db.Column('s_NoticeName', db.String(256))
    OrganReal = db.Column('s_OrganReal', db.String(100))
    colabo = db.Column('s_ColaboClose', db.DateTime)
