import tinydb
from pathlib import Path

class DB:
    def __init__(self, db_path: Path, db_file_prefix: str):
        self._db = tinydb.TinyDB(db_path / f"{db_file_prefix}.json", create_dirs=False)

    def create(self, item: dict) -> int:
        card_id = self._db.insert(item)
        return card_id

    def read(self, card_id: int):
        item = self._db.get(doc_id=card_id)
        return item

    def read_all(self):
        return self._db

    def update(self, card_id: int, mods: dict) -> None:
        changes = {k: v for k, v in mods.items() if v is not None}
        self._db.update(changes, doc_ids=[card_id])

    def delete(self, card_id: int) -> None:
        self._db.remove(doc_ids=[card_id])

    def delete_all(self) -> None:
        self._db.truncate()

    def count(self) -> int:
        return len(self._db)

    def close(self):
        self._db.close()
