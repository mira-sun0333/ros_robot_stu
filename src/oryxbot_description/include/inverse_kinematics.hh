#include "global_constants.hh"
#include <geometry_msgs/Point.h>
bool inverse_kinematics(double position[3], double angle[3])
    {
	float x = position[0];
	float y = position[1];
	float z = position[2];
	float xIn, zIn, phi, rightAll, sqrtZX = 0.0;
	float angleRot, angleLeft, angleRight = 0.0;
	
	z += 74.55;
	zIn = (z - MATH_L1) / MATH_LOWER_ARM;
	
	// calculate value of theta1: the rotation angle
	if (y == 0)
		angleRot = 90;
	else if (y < 0)
		angleRot = -atan(x / y) * deg2rad;
	else if (y > 0)
		angleRot = 180 - atan(x / y) * deg2rad;

	// 使用 sqrt(x*x + y*y) 替代 x / sin(angleRot) 消除奇点
	// 数学上等价: x / sin(angleRot/deg2rad) = sqrt(x^2 + y^2)
	float r_horizontal = sqrt(x * x + y * y);
	xIn 	= (r_horizontal - MATH_L2 - 56.55) / MATH_LOWER_ARM;

	// 检查 xIn 有效性
	if (xIn <= 0)
	{
		ROS_ERROR("Target too close to base! r_horizontal=%.2f", r_horizontal);
		return false;
	}

	phi 	= atan(zIn / xIn) * deg2rad;
	sqrtZX 	= sqrt(zIn * zIn + xIn * xIn);

	if (sqrtZX < 1e-6)
	{
		ROS_ERROR("Invalid sqrtZX value!");
		return false;
	}

	rightAll   = (sqrtZX * sqrtZX + MATH_UPPER_LOWER * MATH_UPPER_LOWER  - 1) 
			   / (2 * MATH_UPPER_LOWER  * sqrtZX);

	if (rightAll < -1.0 || rightAll > 1.0)
	{
		ROS_ERROR("Target out of reach! sqrtZX=%.3f", sqrtZX);
		return false;
	}

	angleRight = acos(rightAll) * deg2rad;

	// calculate value of theta2 and theta3
	rightAll   = (sqrtZX * sqrtZX + 1 - MATH_UPPER_LOWER * MATH_UPPER_LOWER ) / (2 * sqrtZX);

	if (rightAll < -1.0 || rightAll > 1.0)
	{
		ROS_ERROR("Target out of reach (left arm)! sqrtZX=%.3f", sqrtZX);
		return false;
	}

	angleLeft  = acos(rightAll) * deg2rad;
	angleLeft  = angleLeft + phi;
	angleRight = angleRight - phi;

	if (isnan(angleRot) || isnan(angleLeft) || isnan(angleRight))
        {
            ROS_ERROR("Inverse kinematic could not be calculated!");
            return false;
        }

	angle[0] = angleRot;
	angle[1] = angleLeft;
	angle[2] = angleRight;
	return true;
    }
