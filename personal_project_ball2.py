ó
ê,|\c           @   s$   d  d l  Td e f d     YZ d S(   iÿÿÿÿ(   t   *t   Ballc           B   s#   e  Z d    Z d   Z d   Z RS(   c         C   s   t  j |   |  j   |  j   |  _ |  j   |  _ | |  _ | |  _ | |  _	 | |  _
 |  j d  |  j | d  |  j |  |  j | |  d  S(   Nt   circlei
   (   t   Turtlet   __init__t   penupt   xcort   xt   ycort   yt   dxt   dyt   rt
   CanBeEatent   shapet	   shapesizet   colort   goto(   t   selfR   R	   R
   R   R   R   R   (    (    s5   /home/student/Desktop/Agario/personal_project_ball.pyR      s    
				c         C   sþ   | |  _  | |  _ |  j   } | |  j } |  j   } | |  j } | |  j } | |  j } | |  j }	 | |  j }
 |  j | |  | | k r¤ |  j |  _ n  | | k rÁ |  j |  _ n  |	 | k rÝ |  j |  _ n  |
 | k rú |  j |  _ n  d  S(   N(   t   screen_widtht   screen_heightR   R
   R   R   R   R   (   R   R   R   t	   current_xt   new_xt	   current_yt   new_yt   right_side_ballt   left_side_ballt   up_side_ballt   bottom_side_ball(    (    s5   /home/student/Desktop/Agario/personal_project_ball.pyt   move   s&    		c         C   s   |  j    |  j | |  |  j   |  _ |  j   |  _ | |  _ | |  _ | |  _ |  j	 d  |  j
 | d  |  j |  d  S(   NR   i
   (   R   R   R   R   R   R	   R
   R   R   R   R   R   (   R   R   R	   R
   R   R   R   (    (    s5   /home/student/Desktop/Agario/personal_project_ball.pyt   new_Ball)   s    
			(   t   __name__t
   __module__R   R   R   (    (    (    s5   /home/student/Desktop/Agario/personal_project_ball.pyR      s   		N(   t   turtleR   R   (    (    (    s5   /home/student/Desktop/Agario/personal_project_ball.pyt   <module>   s   
