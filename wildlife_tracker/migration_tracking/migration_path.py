from typing import Optional

from ..habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                path_id: int,
                species: str,
                start_location: Habitat,
                destination: Habitat,
                duration: Optional[int] = None) -> None:
          self.path_id = path_id
          self.species = species
          self.start_location = start_location
          self.destination = destination
          self.duration = duration
        

def update_migration_path_details(self, **kwargs) -> None:
    pass

def get_migration_path_by_id(self) -> MigrationPath:
    pass

def get_migration_paths(self) -> list[MigrationPath]:
    pass

def get_migration_paths_by_destination(self) -> list[MigrationPath]:
    pass

def get_migration_paths_by_species(self) -> list[MigrationPath]:
    pass

def get_migration_paths_by_start_location(self) -> list[MigrationPath]:
    pass

def get_migration_paths(self) -> list[MigrationPath]:
    pass