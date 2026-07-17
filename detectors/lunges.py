from core.base_exercise import BaseExercise


class LungesDetector(BaseExercise):
    DOWN_THRESHOLD = 90  # ✅ Changed
    UP_THRESHOLD = 140  # ✅ Changed
    MIN_VISIBILITY = 0.5  # ✅ Changed

    LEFT_HIP = 23
    LEFT_KNEE = 25
    LEFT_ANKLE = 27
    RIGHT_HIP = 24
    RIGHT_KNEE = 26
    RIGHT_ANKLE = 28
    LEFT_SHOULDER = 11
    RIGHT_SHOULDER = 12

    def __init__(self):
        super().__init__()

    def reset(self) -> None:
        self.reps = 0
        self.stage = None

    def process(self, landmarks) -> dict:
        left_knee_angle = self.calculate_angle(
            self.get_point(landmarks, self.LEFT_HIP),
            self.get_point(landmarks, self.LEFT_KNEE),
            self.get_point(landmarks, self.LEFT_ANKLE),
        )

        right_knee_angle = self.calculate_angle(
            self.get_point(landmarks, self.RIGHT_HIP),
            self.get_point(landmarks, self.RIGHT_KNEE),
            self.get_point(landmarks, self.RIGHT_ANKLE),
        )

        if left_knee_angle <= right_knee_angle:
            front_knee_angle = left_knee_angle
            front_hip_idx = self.LEFT_HIP
            front_knee_idx = self.LEFT_KNEE
            front_ankle_idx = self.LEFT_ANKLE
            shoulder_idx_for_torso = self.LEFT_SHOULDER
        else:
            front_knee_angle = right_knee_angle
            front_hip_idx = self.RIGHT_HIP
            front_knee_idx = self.RIGHT_KNEE
            front_ankle_idx = self.RIGHT_ANKLE
            shoulder_idx_for_torso = self.RIGHT_SHOULDER

        key_landmarks_visible = landmarks[front_hip_idx].visibility > self.MIN_VISIBILITY and landmarks[front_knee_idx].visibility > self.MIN_VISIBILITY and landmarks[front_ankle_idx].visibility > self.MIN_VISIBILITY

        if key_landmarks_visible:
            if self.stage is None:
                if front_knee_angle < self.DOWN_THRESHOLD:
                    self.stage = "down"
                elif front_knee_angle > self.UP_THRESHOLD:
                    self.stage = "up"
            
            elif self.stage == "down":
                if front_knee_angle > self.UP_THRESHOLD:
                    self.stage = "up"
            
            elif self.stage == "up":
                if front_knee_angle < self.DOWN_THRESHOLD:
                    self.stage = "down"
                    self.reps += 1
                    print(f"✅ REP: {self.reps} | ANGLE: {front_knee_angle:.1f}°")

        torso_angle = self.calculate_angle(
            self.get_point(landmarks, shoulder_idx_for_torso),
            self.get_point(landmarks, front_hip_idx),
            self.get_point(landmarks, front_knee_idx),
        )

        shoulder_mid_x = (landmarks[self.LEFT_SHOULDER].x + landmarks[self.RIGHT_SHOULDER].x) / 2
        hip_mid_x = (landmarks[self.LEFT_HIP].x + landmarks[self.RIGHT_HIP].x) / 2
        lateral_offset = abs(shoulder_mid_x - hip_mid_x)

        if lateral_offset <= 0.08:
            balance_status = "BALANCED"
        else:
            balance_status = "OFF BALANCE"

        return {
            "reps": self.reps,
            "front_knee_angle": int(front_knee_angle),
            "torso_angle": int(torso_angle),
            "balance_status": balance_status,
        }
