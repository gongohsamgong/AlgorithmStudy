import collections

def solution(participant, completion):
    answer = ""
    participant_count = collections.Counter(participant)
    completion_count = collections.Counter(completion)
    missing_participant = participant_count - completion_count
    answer = missing_participant.elements().__next__()
    return answer
