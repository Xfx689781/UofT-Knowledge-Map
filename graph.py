from collections import defaultdict
from data import courses

concept_to_courses = defaultdict(set)
concept_links = defaultdict(set)
domain_to_courses = defaultdict(set)


def norm(x):
    return x.strip().lower()


# build graph
for course, info in courses.items():
    domains = info["domain"]
    topics = [norm(t) for t in info["topics"]]

    for d in domains:
        domain_to_courses[d].add(course)

    # concept → course mapping
    for t in topics:
        concept_to_courses[t].add(course)

    # intra-course links
    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            a, b = topics[i], topics[j]
            concept_links[a].add(b)
            concept_links[b].add(a)


def get_concept(concept):
    c = norm(concept)

    return {
        "concept": c,
        "courses": list(concept_to_courses.get(c, [])),
        "related": list(concept_links.get(c, []))[:10]
    }


def get_domain(domain):
    d = norm(domain)
    return {
        "domain": d,
        "courses": list(domain_to_courses.get(d, []))
    }