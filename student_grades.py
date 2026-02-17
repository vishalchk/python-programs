# =============================
# Student Grade Management 🏫
# Enhanced Version 2.0 🚀
# =============================

# 1. Create Lists
students = ["John", "Mary", "Bob", "Lisa", "Charlie"]
scores =   [85,     92,     78,    95,     88]
subjects = ["Math", "Science", "English"]
subject_scores = {
    "John":    [85, 88, 82],
    "Mary":    [92, 90, 94],
    "Bob":     [78, 75, 80],
    "Lisa":    [95, 98, 92],
    "Charlie": [88, 85, 90]
}

# =============================
# FEATURE 1 — Grade Calculator 🎓
# =============================
def get_grade(score):
    if score >= 90:
        return "A 🌟"
    elif score >= 80:
        return "B ✅"
    elif score >= 70:
        return "C ⚠️"
    elif score >= 60:
        return "D ❌"
    else:
        return "F 💔"

# =============================
# FEATURE 2 — Search Student 🔍
# =============================
def search_student(name):
    if name in students:
        index = students.index(name)
        score = scores[index]
        grade = get_grade(score)
        print(f"\n🔍 Student Found!")
        print(f"   Name  : {name}")
        print(f"   Score : {score}")
        print(f"   Grade : {grade}")
        if name in subject_scores:
            print(f"   Subjects:")
            for i, subject in enumerate(subjects):
                print(f"     - {subject}: {subject_scores[name][i]}  Grade: {get_grade(subject_scores[name][i])}")
    else:
        print(f"\n❌ Student '{name}' not found!")

# =============================
# FEATURE 3 — Update Score ✏️
# =============================
def update_score(name, new_score):
    if name in students:
        index = students.index(name)
        old_score = scores[index]
        scores[index] = new_score
        print(f"\n✏️  Score Updated!")
        print(f"   Student  : {name}")
        print(f"   Old Score: {old_score}  Grade: {get_grade(old_score)}")
        print(f"   New Score: {new_score}  Grade: {get_grade(new_score)}")
    else:
        print(f"\n❌ Student '{name}' not found!")

# =============================
# MAIN PROGRAM
# =============================

print("=" * 45)
print("   STUDENT GRADE MANAGEMENT 🏫 v2.0 🚀")
print("=" * 45)

# Print all students with grades
print("\n📋 Class Roll Call:")
for i in range(len(students)):
    grade = get_grade(scores[i])
    print(f"   {i+1}. {students[i]:10} Score: {scores[i]}  Grade: {grade}")

# Total students
print(f"\n👥 Total Students: {len(students)}")

# Scoreboard
print("\n🏆 Scoreboard:")
print(f"   - Highest Score: {max(scores)}")
print(f"   - Lowest Score : {min(scores)}")
print(f"   - Average Score: {sum(scores) // len(scores)}")

# Subject Wise Scores
print("\n📚 Subject Wise Scores:")
print(f"   {'Student':10}", end="")
for subject in subjects:
    print(f"  {subject:10}", end="")
print("  Average  Grade")
print("   " + "-" * 55)
for student in students:
    if student in subject_scores:
        s_scores = subject_scores[student]
        avg = sum(s_scores) // len(s_scores)
        grade = get_grade(avg)
        print(f"   {student:10}", end="")
        for s in s_scores:
            print(f"  {s:<10}", end="")
        print(f"  {avg}       {grade}")

# Grade Distribution
print("\n🎓 Grade Distribution:")
grade_count = {"A 🌟": 0, "B ✅": 0, "C ⚠️": 0, "D ❌": 0, "F 💔": 0}
for score in scores:
    grade = get_grade(score)
    grade_count[grade] += 1
for grade, count in grade_count.items():
    print(f"   Grade {grade}: {count} students")

# Search Student
print("\n" + "=" * 45)
print("   🔍 SEARCH STUDENT FEATURE")
print("=" * 45)
search_student("Lisa")
search_student("Alex")

# Update Score
print("\n" + "=" * 45)
print("   ✏️  UPDATE SCORE FEATURE")
print("=" * 45)
update_score("Bob", 85)

# Final List
print("\n📋 Final Student List:")
for i in range(len(students)):
    grade = get_grade(scores[i])
    status = "✅ Pass" if scores[i] >= 60 else "❌ Fail"
    print(f"   {i+1}. {students[i]:10} Score: {scores[i]}  Grade: {grade}  {status}")

# Best and worst
best  = students[scores.index(max(scores))]
worst = students[scores.index(min(scores))]
print(f"\n🥇 Best Student : {best}  Score: {max(scores)}  Grade: {get_grade(max(scores))}")
print(f"🥉 Worst Student: {worst}  Score: {min(scores)}  Grade: {get_grade(min(scores))}")

print("\n" + "=" * 45)
print("       PROGRAM COMPLETE 🎉")
print("=" * 45)
