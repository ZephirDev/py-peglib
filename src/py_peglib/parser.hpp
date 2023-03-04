#pragma once

#include <boost/python.hpp>

#include <peglib.h>

namespace py_peglib {

    class parser {

        peg::parser lib_parser;

    public:

        parser(const std::string& language);

        virtual ~parser() = default;

        void enable_packrat_parsing();

        bool isValid();

        void on(const std::string& keyword, boost::python::object lambda);

        boost::python::object parse(const std::string& value);
    };

}
