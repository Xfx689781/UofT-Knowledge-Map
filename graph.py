from collections import defaultdict
from data import courses

concept_to_courses = defaultdict(set)
concept_links = defaultdict(set)
domain_to_courses = defaultdict(set)

# normalize helper
def norm(s):
    return s.strip().lower()

for course, info in courses.items():
    domains = info["domain"]
    topics = [norm(t) for t in info["topics"]]

    for d in domains:
        domain_to_courses[d].add(course)

    for t in topics:
        concept_to_courses[t].add(course)

    # cross-topic links (same course)
    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            a, b = topics[i], topics[j]
            concept_links[a].add(b)
            concept_links[b].add(a)

# 🔥 NEW: cross-course concept merging
concept_to_courses = defaultdict(set, {
    k: set(v) for k, v in concept_to_courses.items()
})