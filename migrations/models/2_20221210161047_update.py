from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(250) USING "password"::VARCHAR(250);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ALTER COLUMN "password" TYPE VARCHAR(50) USING "password"::VARCHAR(50);"""
