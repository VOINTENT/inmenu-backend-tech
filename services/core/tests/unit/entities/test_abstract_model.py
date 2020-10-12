from datetime import datetime
import pytest

from src.internal.biz.entities.abstract_model import AbstractModel


def test_empty_init():
    abstract_model = AbstractModel()

    assert abstract_model.id is None
    assert abstract_model.created_at is None
    assert abstract_model.edited_at is None


def test_correct_init():
    id = 1
    now_date = datetime.now()

    abstract_model = AbstractModel(
        id=id,
        created_at=now_date,
        edited_at=now_date
    )

    assert abstract_model.id == id
    assert abstract_model.created_at == now_date
    assert abstract_model.edited_at == now_date


def test_incorrect_init():
    with pytest.raises(TypeError):
        AbstractModel(id='12')

    with pytest.raises(TypeError):
        AbstractModel(created_at='12-11-1998')

    with pytest.raises(TypeError):
        AbstractModel(edited_at='12-11-1998')


def test_correct_setters():
    id = 1
    now_date = datetime.now()

    abstract_model = AbstractModel()
    abstract_model.id = id
    abstract_model.created_at = now_date
    abstract_model.edited_at = now_date

    assert abstract_model.id == id
    assert abstract_model.created_at == now_date
    assert abstract_model.edited_at == now_date


def test_incorrect_setters():
    abstract_model = AbstractModel()

    with pytest.raises(TypeError):
        abstract_model.id = '12'

    with pytest.raises(TypeError):
        abstract_model.created_at = '12'

    with pytest.raises(TypeError):
        abstract_model.edited_at = '12'


def test_timestamps():
    abstract_model = AbstractModel()
    now_date = datetime.now()
    abstract_model.created_at = abstract_model.edited_at = now_date

    assert abstract_model.created_at_timestamp == round(now_date.timestamp())
    assert abstract_model.edited_at_timestamp == round(now_date.timestamp())
