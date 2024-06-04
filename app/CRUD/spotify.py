from app.DB.database import engineconn
from app.DB.models import SPOTIFY, USERS
from sqlalchemy import *

engine = engineconn()
session_maker = engine.sessionmaker()



async def insert_SpotifyInfo(user_id, access_token, refresh_token, expires_at):
    print(type(user_id), type(access_token), type(refresh_token), type(expires_at))
    try:    
        await session_maker.execute(
            insert(SPOTIFY),
            [
                {
                    'USER_ID': int(user_id),
                    'ACCESS_TOKEN': access_token,
                    'REFRESH_TOKEN': refresh_token,
                    'EXPIRE_DATE': expires_at,
                    'EMOTION': '분노, 상처'
                }
            ]
        )
        await session_maker.commit()
        return True
    except:
        await session_maker.rollback()
        return False
    finally:
        await session_maker.close()

def update_refreshtoken(user_id, access_token, expires_at):
    try:
        session_maker.execute(
            update(SPOTIFY)
            .where(SPOTIFY.USER_ID == user_id)
            .values(
                {
                    SPOTIFY.ACCESS_TOKEN : access_token,
                    SPOTIFY.EXPIRE_DATE : expires_at
                }
            )
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()

def update_emotion(user_id, emotion):
    try:
        session_maker.execute(
            update(SPOTIFY)
            .where(SPOTIFY.USER_ID == user_id)
            .values(
                {
                    SPOTIFY.EMOTION : emotion
                }
            )
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()



def update_spotify_status(user_id):
    try:
        session_maker.execute(
            update(SPOTIFY)
            .where(USERS.USER_ID == user_id)
            .values(
                {
                    USERS.SPOTIFY: 1
                }
            )
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()