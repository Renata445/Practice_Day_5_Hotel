import redis
import random

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


random.seed(200)
hotel_rooms = {f"hotel_rooms:{random.getrandbits(32)}": i for i in (
    {
        "id": 1,
        "id_hotel": 1,
        "id_room": 1,
    },
    {
        "id": 2,
        "id_hotel": 2,
        "id_room": 2,
    },
    {
        "id": 3,
        "id_hotel": 3,
        "id_room": 3,
    },
    {
        "id": 4,
        "id_hotel": 4,
        "id_room": 4,
    },
    {
        "id": 5,
        "id_hotel": 5,
        "id_room": 5,
    })
}

with r.pipeline() as pipe:
    for supp, hotel_rooms in hotel_rooms.items():
        pipe.hmset(supp, hotel_rooms)
        pipe.execute()


