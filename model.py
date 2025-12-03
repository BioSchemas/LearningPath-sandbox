# Live coded tutorial / example from Charlie, how we could use Pydantic to model for schemas

from pydantic import BaseModel, Field

from curies import NamedReference
from curies.vocabulary import charlie

charlie = NamedReference(
    prefix="orcid",
    identifier="0000-0000-0000-000X",
    name="Charlie Hoyt"
)

class LearningMaterial(BaseModel):
    title: str
    authors: list[Reference]

class LearningPathModule(BaseModel):
    name: str
    description: str | None
    materials: list[LearningMaterial]

class LearningPath(BaseModel): 
    name: str
    description: str | None = Field(
        None,
        description="This is where you describe the learning path"
    )
    course_code: str | None = None
    modules: list[LearningPathModule]


example = LearningPath(
    name="Introduction to Sequencing",
    modules=[
        LearningPathModule(
            name="Getting Started",
            materials=[
                LearningMaterial(
                    name="Install Python",
                    authors=[charlie],
                )
            ]
        )
    ]
)