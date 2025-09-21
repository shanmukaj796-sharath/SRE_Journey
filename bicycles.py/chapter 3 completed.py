subjects=['maths','chemistery','physics','english','social science','computer science']
print(subjects)
subjects.append('physical education')
print(subjects)
subjects.insert(4,'kannada')
del subjects[5]
popped_subjects=subjects.pop()
print(popped_subjects)
print(subjects)
fav_subj=subjects.pop(5)
print(f"My favourite subject is {fav_subj.title()}.")
print(subjects)
subjects.remove('chemistery')
print(subjects)

print(len(subjects))