from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    id: int
    module_id: int
    title: str
    description: str
    video_url: str

class Module(BaseModel):
    id: int
    course_id: int
    title: str
    description: str
    lessons: List[Lesson]

class Course(BaseModel):
    id: int
    title: str
    description: str
    modules: List[Module]

basic_lesson_1 = Lesson(
    id=1,
    module_id=1,
    title="Variables",
    description="Learn variables in python",
    video_url="https://example.video"
)
basic_lesson_2 = Lesson(
    id=2,
    module_id=1,
    title="Functions",
    description="Learn Functions in python",
    video_url="https://example.video"
)
advance_lesson_1 = Lesson(
    id=3,
    module_id=2,
    title="Iterator",
    description="Learn Iterator in python",
    video_url="https://example.video"
)
advance_lesson_2 = Lesson(
    id=4,
    module_id=2,
    title="Threads and Processes",
    description="Learn Threads and Processes in python",
    video_url="https://example.video"
)
    
py_module_1 = Module(
    id=1,
    course_id=1,
    title="Basics of python",
    description="Learn basics of python",
    lessons=[basic_lesson_1, basic_lesson_2]
)

py_module_2 = Module(
    id=2,
    course_id=1,
    title="Advance of python",
    description="Learn advance of python",
    lessons=[advance_lesson_1, advance_lesson_2]
)

python_course = Course(
    id=1,
    title="Python Tutorial",
    description="Learn python zero to 100",
    modules=[py_module_1, py_module_2]
)

print(python_course.model_dump())
