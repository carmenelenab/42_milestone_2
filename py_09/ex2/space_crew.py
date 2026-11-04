from enum import Enum
from datetime import datetime

try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("\00[31mMissing pydantic dependency\033[0m")
    print("Use: \033[32mpip install pydantic\033[0m")
    exit()


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        commander_ranks = {
            Rank.COMMANDER, Rank.CAPTAIN, "commander", "capitan"
        }
        if not any(m for m in commander_ranks):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced_crew = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experienced_crew < len(self.crew) / 2:
                raise ValueError(
                    r"Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def __str__(self) -> str:
        members = "\n".join(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
            for member in self.crew
        )
        return (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            f"Crew members:\n{members}\n"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    try:
        print("=========================================")
        print("Valid mission created:")

        valid_test = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=33,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
                CrewMember(
                    member_id="002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=57,
                    specialization="Navigation",
                    years_experience=23,
                    is_active=True
                ),
                CrewMember(
                    member_id="003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=33,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
            ],
            budget_millions=2500.0,
        )
        print(valid_test)
    except ValidationError as e:
        for error in e.errors():
            clean_msg = error["msg"].removeprefix("Value error, ")
            print(clean_msg)

    try:
        print("=========================================")
        print("Expected validation error:")

        invalid_test = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="1",
                    name="Sarah Connor",
                    rank=Rank.OFFICER,
                    age=33,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
                CrewMember(
                    member_id="2",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=57,
                    specialization="Navigation",
                    years_experience=23,
                    is_active=True
                ),
                CrewMember(
                    member_id="3",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=33,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
            ],
            budget_millions=2500.0,
        )
        print(invalid_test)
    except ValidationError as e:
        for error in e.errors():
            clean_msg = error["msg"].removeprefix("Value error, ")
            print(clean_msg)


if __name__ == "__main__":
    main()