import aiosqlite, datetime

#=======================================================================
async def create_db():
    async with aiosqlite.connect("thread.db") as db:  # menstrualz ишак бездарный
        cursor = await db.cursor()
        query = '''
        CREATE TABLE IF NOT EXISTS thread(
            ownerid_thread INTEGER,
            code INTEGER,
            threadid INTEGER,
            time INTEGER
        )
        '''
        await cursor.execute(query)
        print("Чики (Приватное Общение) успешно завершено\n Репозиторий - https://github.com/Crone720/GroupTalk-disnake")
        await db.commit()

#=======================================================================

async def get_thread_info(id):
    async with aiosqlite.connect('thread.db') as conn:
        cursor = await conn.cursor()
        await cursor.execute("SELECT * FROM thread WHERE threadid = ?", (id,))
        b = await cursor.fetchall()
        return b


async def get_thread(member):
    async with aiosqlite.connect("thread.db") as db:
        cursor = await db.cursor()
        query = "SELECT threadid FROM thread WHERE ownerid_thread = ?"
        await cursor.execute(query, (member,))
        b = await cursor.fetchone()
        return b[0] if b else None
async def add_thread(ownerid_thread, code, threadid, time):
    async with aiosqlite.connect("thread.db") as db:
        cursor = await db.cursor()
        query = "INSERT INTO thread VALUES(?,?,?,?)"
        await cursor.execute(query, (ownerid_thread, code, threadid, time))
        await db.commit()

async def del_thread(threadid):
    async with aiosqlite.connect("thread.db") as db:
        cursor = await db.cursor()
        query = "DELETE FROM thread WHERE threadid = ?"
        await cursor.execute(query, (threadid,))
        await db.commit()

async def get_code_thread(code):
    async with aiosqlite.connect("thread.db") as db:
        cursor = await db.cursor()
        query = "SELECT threadid FROM thread WHERE code = ?"
        await cursor.execute(query, (code,))
        b = await cursor.fetchone()
        return b[0] if b else None
    
async def get_owner_thread(id):
    async with aiosqlite.connect("thread.db") as db:
        cursor = await db.cursor()
        query = "SELECT ownerid_thread FROM thread WHERE threadid = ?"
        await cursor.execute(query, (id,))
        b = await cursor.fetchone()
        return b[0]