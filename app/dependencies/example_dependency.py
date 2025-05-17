from fastapi import Depends, HTTPException, status
from typing import Optional

# Example dependency function
def get_query_token(token: Optional[str] = None):
    if token != "expected-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return token

# Another example dependency that could be used for user authentication
def verify_user(user_id: int):
    # Simulate user verification logic
    if user_id != 1:  # Assuming 1 is a valid user ID for demonstration
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return {"user_id": user_id, "username": "example_user"}