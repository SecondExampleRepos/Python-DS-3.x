import pandas as pd

#High temp LLM generated
class RaceComparison:
    
    def __init__(self):
        pass

    def compare_speed(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare speeds and return where df1 has higher speed than df2."""
        comparison = df1['GPS Speed (mph)'] > df2['GPS Speed (mph)']
        return df1[comparison]

    def compare_lateral_acceleration(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare lateral acceleration and return where df1 has higher lateral acceleration than df2."""
        comparison = df1['LateralAcc (g)'] > df2['LateralAcc (g)']
        return df1[comparison]

    def compare_longitudinal_acceleration(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare longitudinal acceleration and return where df1 has higher longitudinal acceleration than df2."""
        comparison = df1['GPS LonAcc (g)'] > df2['GPS LonAcc (g)']
        return df1[comparison]

    def compare_yaw_rate(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare yaw rates and return where df1 has lower yaw rate than df2."""
        comparison = df1['YawRate (deg/s)'] < df2['YawRate (deg/s)']
        return df1[comparison]

    def compare_gear(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare gear and return where df1 has higher gear than df2."""
        comparison = df1['Gear (gear)'] > df2['Gear (gear)']
        return df1[comparison]

    def compare_brake_pressure(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare brake pressure and return where df1 has higher brake pressure than df2."""
        comparison = df1['BrakePress (psi)'] > df2['BrakePress (psi)']
        return df1[comparison]

    def compare_rpm(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare RPM and return where df1 has higher RPM than df2."""
        comparison = df1['RPM dup 2 (rpm)'] > df2['RPM dup 2 (rpm)']
        return df1[comparison]

    def compare_steer_angle(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare steer angle and return where df1 has lower steer angle than df2."""
        comparison = df1['SteerAngle (deg)'] < df2['SteerAngle (deg)']
        return df1[comparison]

    def compare_oil_temp(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare oil temperature and return where df1 has lower oil temperature than df2."""
        comparison = df1['OilTemp (°F)'] < df2['OilTemp (°F)']
        return df1[comparison]


    def compare_speed_variation(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """Compare speed variation and return where df1 has higher speed variation than df2."""
        comparison = df1['SpeedV (mph)'] > df2['SpeedV (mph)']
        return df1[comparison]



# Fight each other with this. 