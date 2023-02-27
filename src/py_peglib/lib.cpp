#include <boost/python.hpp>

#include "parser.hpp"
#include "semantic_values.hpp"
#include "info.hpp"

BOOST_PYTHON_MODULE(py_peglib) {
    boost::python::def("get_binding_version", ::py_peglib::get_binding_version);

    boost::python::class_<::py_peglib::parser>("Parser", boost::python::init<std::string>())
        .def("on", &::py_peglib::parser::on)
        .def("parse", &::py_peglib::parser::parse)
    ;

    boost::python::class_<::py_peglib::semantic_values>("SemanticValues", boost::python::no_init)
        .def("size", &::py_peglib::semantic_values::size)
        .def("toString", &::py_peglib::semantic_values::to_string)
    ;
}
