// Generated by gencpp from file xycar_motor/xycar_motor.msg
// DO NOT EDIT!


#ifndef XYCAR_MOTOR_MESSAGE_XYCAR_MOTOR_H
#define XYCAR_MOTOR_MESSAGE_XYCAR_MOTOR_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace xycar_motor
{
template <class ContainerAllocator>
struct xycar_motor_
{
  typedef xycar_motor_<ContainerAllocator> Type;

  xycar_motor_()
    : header()
    , angle(0)
    , speed(0)  {
    }
  xycar_motor_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , angle(0)
    , speed(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _angle_type;
  _angle_type angle;

   typedef int32_t _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::xycar_motor::xycar_motor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::xycar_motor::xycar_motor_<ContainerAllocator> const> ConstPtr;

}; // struct xycar_motor_

typedef ::xycar_motor::xycar_motor_<std::allocator<void> > xycar_motor;

typedef boost::shared_ptr< ::xycar_motor::xycar_motor > xycar_motorPtr;
typedef boost::shared_ptr< ::xycar_motor::xycar_motor const> xycar_motorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::xycar_motor::xycar_motor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::xycar_motor::xycar_motor_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::xycar_motor::xycar_motor_<ContainerAllocator1> & lhs, const ::xycar_motor::xycar_motor_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.angle == rhs.angle &&
    lhs.speed == rhs.speed;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::xycar_motor::xycar_motor_<ContainerAllocator1> & lhs, const ::xycar_motor::xycar_motor_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace xycar_motor

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::xycar_motor::xycar_motor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::xycar_motor::xycar_motor_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xycar_motor::xycar_motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::xycar_motor::xycar_motor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xycar_motor::xycar_motor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::xycar_motor::xycar_motor_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::xycar_motor::xycar_motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "776d1e41053a9ee231920fdd113d2d0a";
  }

  static const char* value(const ::xycar_motor::xycar_motor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x776d1e41053a9ee2ULL;
  static const uint64_t static_value2 = 0x31920fdd113d2d0aULL;
};

template<class ContainerAllocator>
struct DataType< ::xycar_motor::xycar_motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "xycar_motor/xycar_motor";
  }

  static const char* value(const ::xycar_motor::xycar_motor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::xycar_motor::xycar_motor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"int32 angle\n"
"int32 speed\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::xycar_motor::xycar_motor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::xycar_motor::xycar_motor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.angle);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct xycar_motor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::xycar_motor::xycar_motor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::xycar_motor::xycar_motor_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "angle: ";
    Printer<int32_t>::stream(s, indent + "  ", v.angle);
    s << indent << "speed: ";
    Printer<int32_t>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // XYCAR_MOTOR_MESSAGE_XYCAR_MOTOR_H
