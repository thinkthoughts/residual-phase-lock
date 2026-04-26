# src/loop.py
from .residuals import structured_residual
from .phase_lock import is_phase_locked
from .revise import gradient_like_revision

def phase_lock_loop(model, x, target, max_iters=5):
    """
    Residual → phase-lock → revise loop
    """
    y = model(x)

    for _ in range(max_iters):
        r = structured_residual(y, target)

        locked, cos_theta = is_phase_locked(y, target)

        if locked:
            break

        y = gradient_like_revision(y, r)

    return y, cos_theta
