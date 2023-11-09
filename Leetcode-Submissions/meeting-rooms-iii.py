class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        meetings.sort()
        current = []

        freq = [0 for i in range(n)]

        for meeting in meetings:
            while(current and current[0][0]<=meeting[0]):
                end_time,to_be_taken = heapq.heappop(current)
                heappush(rooms,to_be_taken)
                    
            if(len(rooms)>0):
                to_be_taken = heapq.heappop(rooms)
                heapq.heappush(current,[meeting[1],to_be_taken])
            else:
                end_time,to_be_taken = heapq.heappop(current)
                heapq.heappush(current,[meeting[1]+max(0,end_time-meeting[0]),to_be_taken])
            freq[to_be_taken]+=1

        answer = -1
        answer_count = 0
        for index,temp in enumerate(freq):
            if(temp>answer_count):
                answer=index
                answer_count = temp

        return answer