from supabase import create_client, Client

SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-key"

def get_authenticated_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
