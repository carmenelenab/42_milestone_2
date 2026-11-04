from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("\00[31mMissing pydantic dependency\033[0m")
    print("Use: \033[32mpip install pydantic\033[0m")
    exit()


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: None | str = Field(default=None, max_length=200)

    def __str__(self) -> str:
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {'Operational\n' if self.is_operational
                       else 'Not operational\n'}"
        )


def main() -> None:
    print("Space Station Data Validation")
    try:
        print("========================================")
        print("Valid station created:")
        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True
        )
        print(valid)
    except ValidationError as e:
        print(e.errors()[0]['msg'])

    try:
        print("========================================")
        print("Expected validation error:")
        invalid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=3,
            power_level=185.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=False
        )
        print(invalid)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
