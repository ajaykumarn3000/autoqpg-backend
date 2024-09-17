from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from config import FIEF_DOMAIN, FIEF_CLIENT_ID, FIEF_CLIENT_SECRET

fief = FiefAsync(FIEF_DOMAIN, FIEF_CLIENT_ID, FIEF_CLIENT_SECRET)

scheme = OAuth2AuthorizationCodeBearer(
    f"{FIEF_DOMAIN}/authorize",
    f"{FIEF_DOMAIN}/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

auth = FiefAuth(fief, scheme)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/user")
async def get_user(access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated())):
    return access_token_info
