L_used = 0.150             # m, measured with a ruler
odo_turn_deg = 3600        # 10 turns by odometry
real_turn_deg = 3600 - 95  # Rover stopped 95 deg short
L_correct = L_used * odo_turn_deg / real_turn_deg
print(f"corrected wheelbase: {L_correct:.4f} m")
