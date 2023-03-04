#include "semantic_values.hpp"

namespace py_peglib {

    semantic_values::semantic_values(const ::peg::SemanticValues& sv)
        : sv(sv)
    {}

    long semantic_values::size() const
    {
        return sv.size();
    }

    long semantic_values::choice() const
    {
        return sv.choice();
    }

    boost::python::object semantic_values::at(const long& index)
    {
        return std::any_cast<boost::python::object>(sv.at(index));
    }

    const std::string semantic_values::to_string() const
    {
        return sv.token_to_string();
    }
}