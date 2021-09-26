from sqlmodel import create_engine
from sqlmodel import Session
from sqlmodel import SQLModel

from dwsheets.schemas.classes import Class
from seeddata import srd

import dwsheets.models

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)


classes = []
session = Session(engine)
for cls in srd['classes']:
    c = Class(**cls)
    cls = dwsheets.models.classes.Class(
        classobj=c.dict(),
        name=c.name,
    )
    session.add(cls)
    for move in c.moves:
        mv = dwsheets.models.moves.Move(
            move=move.dict(),
            name=move.name,
            type=move.move,
            class_uid=cls.uid,
        )
        session.add(mv)
    if c.spells is not None:
        for spell in c.spells.spell_list:
            session.add(dwsheets.models.spells.Spell(
                spell=spell.dict(),
                name=spell.name,
                class_uid=cls.uid,
            ))
    session.commit()
session.close()
