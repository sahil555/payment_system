from aiokafka import AIOKafkaProducer
import json
from app.core.config import settings

class KafkaProducer:
    def __init__(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
        )

    async def start(self):
        await self.producer.start()

    async def send(self, topic, data):
        await self.producer.send_and_wait(
            topic,
            json.dumps(data).encode("utf-8")
        )

    async def stop(self):
        await self.producer.stop()