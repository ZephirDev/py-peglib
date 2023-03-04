#include <boost/python.hpp>

#include "parser.hpp"
#include "semantic_values.hpp"
#include "info.hpp"

BOOST_PYTHON_MODULE(py_peglib) {
    boost::python::def("get_binding_version", ::py_peglib::get_binding_version);

    boost::python::class_<::py_peglib::parser>("Parser", boost::python::init<std::string>())
        .def("enable_packrat_parsing", &::py_peglib::parser::enable_packrat_parsing)
        .def("isValid", &::py_peglib::parser::isValid)
        .def("on", &::py_peglib::parser::on)
        .def("parse", &::py_peglib::parser::parse)
    ;

    boost::python::class_<::py_peglib::semantic_values>("SemanticValues", boost::python::no_init)
        .def("size", &::py_peglib::semantic_values::size)
        .def("choice", &::py_peglib::semantic_values::choice)
        .def("toString", &::py_peglib::semantic_values::to_string)
        .def("at", &::py_peglib::semantic_values::at)
    ;
}
