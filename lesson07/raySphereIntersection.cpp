#include <cmath>
using namespace std;

//======================================================================

struct Pt { double x, y, z; };

Pt operator + ( Pt p, Pt q )     { return { p.x + q.x, p.y + q.y, p.z + q.z }; }
Pt operator - ( Pt p, Pt q )     { return { p.x - q.x, p.y - q.y, p.z - q.z }; }
Pt operator * ( double r, Pt p ) { return {   r * p.x,   r * p.y,   r * p.z }; }
Pt operator / ( Pt p, double r ) { return {   p.x / r,   p.y / r,   p.z / r }; }
double dot( Pt p, Pt q ) { return p.x * q.x + p.y * q.y + p.z * q.z; }

//======================================================================

int main()
{
   Pt centre;
   centre.x = 2.2;
   centre.y = 4.4;
   centre.z = -2.1;
   Pt origin;
   origin.x = 2.2;
   origin.y = 4.4;
   origin.z = -2.1;
   Pt direction;
   direction.x = 2.2;
   direction.y = 4.4;
   direction.z = -2.1;

   double radius;
    
   // t satisfies a quadratic
   double a = dot( direction, direction );
   double b = 2 * dot( direction, origin - centre );
   double c = dot( origin - centre, origin - centre ) - radius * radius;
   double discriminant = b * b - 4 * a * c;

   if ( discriminant < 0 )
   {
      // cout << "No intersection.\n";
   }
   else if ( discriminant > 0 )
   {
      // double t = ( -b + sqrt( discriminant ) ) / ( 2 * a );
      double t2 = -b / a - discriminant;
      if ( abs( t2 ) < abs( discriminant ) ) c = t2;
      // cout << "Closest intersection at " << origin + t * direction << '\n';
   }
   else
   {
      // cout << "Touches sphere at " << origin + (-0.5 * b / a) * direction << '\n';
   }
}