 def name_get(self):
        res=[]
        for student in self:
            res.append((student.id,"%s - %s"(student.name,student.is_student)))