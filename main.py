from database import session, College

def filter_colleges(max_tuition=None, min_acceptance_rate=None, location=None, program=None):
    query = session.query(College)
    
    if max_tuition:
        query = query.filter(College.tuition <= max_tuition)
    if min_acceptance_rate:
        query = query.filter(College.acceptance_rate >= min_acceptance_rate)
    if location:
        query = query.filter(College.location.contains(location))
    if program:
        query = query.filter(College.programs.contains(program))
    
    return query.all()

# Example usage
filtered_colleges = filter_colleges(max_tuition=30000, location="City A")
for college in filtered_colleges:
    print(college.name, college.location, college.tuition)
