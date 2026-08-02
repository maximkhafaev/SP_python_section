from database import Database

db = Database('postgresql://maximkhafaev@localhost:5432/qa')


def test_insert_entity():
    id = db.get_max_id("subject", "subject_id") + 1
    subject_name = 'Astronomy'
    db.add_subject(id, subject_name)
    new_subject = db.get_subject_by_id(id)
    db.delete_subject_by_id(id)

    assert len(new_subject) == 1
    assert new_subject[0]['subject_id'] == id
    assert new_subject[0]['subject_title'] == subject_name


def test_update_entity():
    id = db.get_max_id("users", "user_id") + 1
    user_email = 'test@qa.com'
    db.create_user(id, user_email, 1)
    new_subject_id = 13
    db.update_user(new_subject_id, id)
    updated_user = db.get_user_by_id(id)
    db.delete_user_by_id(id)

    assert updated_user[0]['user_id'] == id
    assert updated_user[0]['user_email'] == user_email
    assert updated_user[0]['subject_id'] == new_subject_id


def test_delete_entity():
    id = db.get_max_id("users", "user_id") + 1
    user_email = 'test@qa.com'
    db.create_user(id, user_email, 10)
    rows = db.get_user_by_id(id)
    assert len(rows) == 1

    db.delete_user_by_id(id)
    rows = db.get_user_by_id(id)

    assert len(rows) == 0
