#! /usr/bin/env ruby
# coding: cp932
a = 1.0
e = 0.0
L = 1.0      
g = 1250.0   
F = 1360.0
R = (F/(g*L))**0.5
#cos1 = (-x+y**0.5)/z
#cos2 = (-x-y**0.5)/z

 while a < 10 do
   while e < 1 do
    #print(R**2)
    #print("\n")
    x = e*e*(4*(a**4)*(1-e*e)-2*(a*a-R*R)*(R*R-a*a*e*e))#b
    #print(x)
    #print("\n")
    y = x*x - 4*(e**4)*( -4*a**4+4*(a**4)*e**2-(a**4)*(e**4)+2*a*a*e*e*R*R-R**4)*(-a**4+2*a*a*R*R-R**4) #b^2-4ac
    #print(y)
    #print("\n")
    z = 2*(e**4)*( -4*a**4+4*(a**4)*e**2-(a**4)*(e**4)+2*a*a*e*e*R*R-R**4)  #2a
    #print(z)
    #print("\n")
    if 0 <= y then
    cos1= ((-x+y**0.5)/z)**0.5
    cos2= ((-x-y**0.5)/z)**0.5
    cos3= -((-x+y**0.5)/z)**0.5
    cos4= -((-x-y**0.5)/z)**0.5
    num1 = cos1.abs
    num2 = cos2.abs
    num3 = cos3.abs
    num4 = cos4.abs
    if num1 <= 1 then
      rad1 = Math.acos(cos1)
      sin2rad1 = Math.sin(2*rad1)
      cos2rad1 = Math.cos(2*rad1)
      sin1 = Math.sin(rad1)
      atan1 = Math.atan(((1-e*e)**0.5-1)*sin2rad1/
                        ((1-e**2)**0.5+1+((1-e**2)**0.5-1)*cos2rad1))
       s11 = 0.5* a*a*(1-e*e)**0.5 *(rad1-atan1)
       s21 = 0.5*a*e*a*((1-e*e)**0.5)*sin1/(1-e*e*cos1*cos1)**0.5
     #  if 0 <= cos1 then
     #  if rad1 <= 3.14 then
        t1 = 1 - 2*(s11 - s21)/(3.14*a*a*(1-e*e)**0.5)
      print(a)
      print(",")
      print(e)
      print(",") 
      print(t1)
      print(",")
      print(rad1)
      print(" ")
      print("\n")
   #    end
   #    end
    end
    if num2 <= 1 then
       rad2 = Math.acos(cos2)
      sin2rad2 = Math.sin(2*rad2)
      cos2rad2 = Math.cos(2*rad2)
      sin2 = Math.sin(rad2)
      atan2 = Math.atan(((1-e*e)**0.5-1)*sin2rad2/
                       ((1-e**2)**0.5+1+((1-e**2)**0.5-1)*cos2rad2))
       s12 = 0.5* a*a*(1-e*e)**0.5 *(rad2-atan2)
       s22 = 0.5*a*e*a*((1-e*e)**0.5)*sin2/(1-e*e*cos2*cos2)**0.5
    #   if 0 <= cos2 then
    #   if rad2 <= 3.14 then
         t2 =1 - 2*(s12-s22)/( 3.14*a*a*(1-e*e)**0.5 )
      print(a)
      print(",")
      print(e)
      print(",") 
      print(t2)
      print(" ")
  #   print(rad2)
  #   print(" ")
      print("\n")
    #   end
    #   end
    end
    if num3 <= 1 then
       rad3 = Math.acos(cos3)
      sin2rad3 = Math.sin(2*rad3)
      cos2rad3 = Math.cos(2*rad3)
      sin3 = Math.sin(rad3)
      atan3 = Math.atan( ( (1-e*e)**0.5-1 )*sin2rad3/
                       ((1-e**2)**0.5+1+((1-e**2)**0.5-1)*cos2rad3))
       s13 = 0.5* a*a*(1-e*e)**0.5 *(rad3-atan3)
       s23 = 0.5*a*e*a*((1-e*e)**0.5)*sin3/(1-e*e*cos3*cos3)**0.5
       if 0 <= cos3 then
       if rad3 <= 3.14 then
        t3 =2*(s13-s23)/( 3.14*a**2*(1-e*e)**0.5)
      print(a)
      print(",")
      print(e)
      print(",") 
      print(t3)
      print(" ")
     # print(rad3)
     # print(" ")
      print("\n")
       end
       end
    end
    if num4 <= 1 then
       rad4 = Math.acos(cos4)
      sin2rad4 = Math.sin(2*rad4)
      cos2rad4 = Math.cos(2*rad4)
      sin4 = Math.sin(rad4)
      atan4 = Math.atan( ( (1-e*e)**0.5-1 )*sin2rad4/
                        ((1-e**2)**0.5+1+((1-e**2)**0.5-1)*cos2rad4))
       s14 = 0.5* a*a*(1-e*e)**0.5 *(rad2-atan4)
       s24 = 0.5*a*e*a*((1-e*e)**0.5)*sin4/(1-e*e*cos4*cos4)**0.5
        if 0 <= cos4 then
       if rad4 <= 3.14 then
         t4 =2*(s14-s24)/( 3.14*a**2*(1-e*e)**0.5 )
      print(a)
      print(",")
      print(e)
      print(",") 
      print(t4)
      print(" ")
    # print(rad4)
    # print(" ")
      print("\n")
       end
        end
    end
    end
    #rad1 = Math.acos(cos1)
    #print("rad1=")
    #print(rad1)
    #print("\n")
    #rad2 = Math.acos(cos2)
    #print("rad2=")
    #print(rad2)
    #print("\n")
    #sin1 = (1-(cos1)**2)**0.5
    #print("sin1=")
    #print(sin1)
    #print("\n")
    #sin2 = (1-(cos2)**2)**0.5
    #print("sin2=")
    #print(sin2)
    #print("\n")
   e = e + 0.05
   end
   a = a + 0.5
   e = 0.0
end
