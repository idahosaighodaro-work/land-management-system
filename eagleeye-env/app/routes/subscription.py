@app.post("/subscribe")
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_sub = Subscription(
        user_id=current_user.id,
        plan=subscription.plan,
        end_date=subscription.end_date
    )
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return {"message": "Subscription created", "subscription": new_sub}
