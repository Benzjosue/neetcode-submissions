class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        rejects = 0

        if not students:
            return 0
        

        
        while sandwiches and rejects < len(students):
            sandwhich = sandwiches[0]

            student = students[0]

            if student == sandwhich:
                students.pop(0)
                sandwiches.pop(0)
                rejects =0
                

            else:
                moved = students.pop(0)
                students.append(moved)
                rejects +=1

        return len(students)