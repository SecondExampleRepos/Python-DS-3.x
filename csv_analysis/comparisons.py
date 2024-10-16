import pandas as pd
from typing import TypeVar, Generic, Self, LiteralString

# Define a type variable for DataFrame
T = TypeVar('T', bound=pd.DataFrame)

# High temp LLM generated
class RaceComparison(Generic[T]):

    def __init__(self: Self) -> None:
        pass

    def compare_speed(self: Self, df1: T, df2: T) -> T:
        """Compare speeds and return where df1 has higher speed than df2."""
        try:
            comparison = df1['GPS Speed (mph)'] > df2['GPS Speed (mph)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_lateral_acceleration(self: Self, df1: T, df2: T) -> T:
        """Compare lateral acceleration and return where df1 has higher lateral acceleration than df2."""
        try:
            comparison = df1['LateralAcc (g)'] > df2['LateralAcc (g)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_longitudinal_acceleration(self: Self, df1: T, df2: T) -> T:
        """Compare longitudinal acceleration and return where df1 has higher longitudinal acceleration than df2."""
        try:
            comparison = df1['GPS LonAcc (g)'] > df2['GPS LonAcc (g)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_yaw_rate(self: Self, df1: T, df2: T) -> T:
        """Compare yaw rates and return where df1 has lower yaw rate than df2."""
        try:
            comparison = df1['YawRate (deg/s)'] < df2['YawRate (deg/s)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_gear(self: Self, df1: T, df2: T) -> T:
        """Compare gear and return where df1 has higher gear than df2."""
        try:
            comparison = df1['Gear (gear)'] > df2['Gear (gear)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_brake_pressure(self: Self, df1: T, df2: T) -> T:
        """Compare brake pressure and return where df1 has higher brake pressure than df2."""
        try:
            comparison = df1['BrakePress (psi)'] > df2['BrakePress (psi)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_rpm(self: Self, df1: T, df2: T) -> T:
        """Compare RPM and return where df1 has higher RPM than df2."""
        try:
            comparison = df1['RPM dup 2 (rpm)'] > df2['RPM dup 2 (rpm)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_steer_angle(self: Self, df1: T, df2: T) -> T:
        """Compare steer angle and return where df1 has lower steer angle than df2."""
        try:
            comparison = df1['SteerAngle (deg)'] < df2['SteerAngle (deg)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_oil_temp(self: Self, df1: T, df2: T) -> T:
        """Compare oil temperature and return where df1 has lower oil temperature than df2."""
        try:
            comparison = df1['OilTemp (°F)'] < df2['OilTemp (°F)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

    def compare_speed_variation(self: Self, df1: T, df2: T) -> T:
        """Compare speed variation and return where df1 has higher speed variation than df2."""
        try:
            comparison = df1['SpeedV (mph)'] > df2['SpeedV (mph)']
            return df1[comparison]
        except KeyError as e:
            e.add_note(f"Missing column in DataFrame: {e}")
            raise

# Fight each other with this.
