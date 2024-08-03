# Apache Airflow Parameters

## Order of Precedence

When working with parameters in Apache Airflow, the order of precedence determines which value is used when multiple sources of parameters are involved. Here’s how Airflow resolves parameter values based on their sources:

1. **Runtime Parameters**:
   - **Definition**: Parameters provided when triggering a DAG run via the Airflow UI, CLI, or API.
   - **Precedence**: Highest. Overrides any default or task-level parameters.

2. **Task-Level Parameters**:
   - **Definition**: Parameters defined directly in the task using the `params` argument in the task definition.
   - **Precedence**: Higher than DAG-level parameters but lower than runtime parameters. Overrides DAG-level parameters for that specific task.

3. **DAG-Level Parameters**:
   - **Definition**: Parameters defined in the DAG using the `params` argument in the DAG definition.
   - **Precedence**: Base values. Can be overridden by task-level and runtime parameters.

# Apache Airflow `Param` Class

The `Param` class in Apache Airflow is used to define and validate parameters for DAGs and tasks in a structured manner. It enhances the flexibility and safety of parameter handling by allowing you to specify types, default values, and constraints.

## Key Features of `Param`

1. **Parameter Validation**
   - Ensures that parameters conform to expected data types and constraints.
   - Provides built-in validation to prevent errors due to invalid data.

2. **Default Values**
   - Allows setting default values for parameters, which will be used if no other values are provided.

3. **Description**
   - Provides a way to document the purpose and usage of each parameter.

4. **Constraints**
   - Supports constraints for numeric values (e.g., minimum and maximum) and specific formats for strings.

## Using `Param`

To use the `Param` class, you define parameters in the DAG with the `params` argument, specifying `Param` instances for each parameter. This allows for clear documentation and validation.
