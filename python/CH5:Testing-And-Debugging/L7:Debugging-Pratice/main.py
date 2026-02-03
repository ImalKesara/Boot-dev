def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp - ach_xp
    alert = f"Achievement unlocked: {ach_name}"
    return after_xp, alert
