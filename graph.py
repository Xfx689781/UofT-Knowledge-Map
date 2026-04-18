from collections import defaultdict
from data import courses

concept_to_courses = defaultdict(set)
domain_to_courses = defaultdict(set)
concept_links = defaultdict(set)


for course, info in courses.items():
    domains = info["domain"]
    topics = info["topics"]

    for d in domains:
        domain_to_courses[d].add(course)

    for t in topics:
        concept_to_courses[t].add(course)

    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            a, b = topics[i], topics[j]
            concept_links[a].add(b)
            concept_links[b].add(a)


def get_concept(concept):
    return {
        "concept": concept,
        "courses": list(concept_to_courses.get(concept, [])),
        "related": list(concept_links.get(concept, []))[:8]
    }


def get_domain(domain):
    return {
        "domain": domain,
        "courses": list(domain_to_courses.get(domain, []))
    }