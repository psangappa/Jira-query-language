# Jira-query-language
Get Jira issues from JQL. A program which takes JQL as its input and gives all the jira issues.

**Constructing JQL queries:**

A simple query in JQL (also known as a 'clause') consists of a field, followed by an operator, followed by one or more values or functions. For example:

project = "TEST"
This query will find all issues in the "TEST" project. It uses the "project" field, the EQUALS operator, and the value "TEST".

**A more complex query might look like this:**

project = "TEST" AND assignee = currentuser()
This query will find all issues in the "TEST" project where the assignee is the currently logged in user. It uses the "project" field, the EQUALS operator, the value "TEST",the "AND" keyword and the "currentuser()" function.

For more information on fields, operators, keywords and functions, see the Reference section below.

**Setting the precedence of operators**

You can use parentheses in complex JQL statements to enforce the precedence of operators.

For example, if you want to find all resolved issues in the 'SysAdmin' project, as well as all issues (any status, any project) currently assigned to the system administrator (bobsmith), you can use parentheses to enforce the precedence of the boolean operators in your query, i.e.

(status=resolved AND project=SysAdmin) OR assignee=bobsmith
Note that if you do not use parentheses, the statement will be evaluated left-to-right.

You can also use parentheses to group clauses, so that you can apply the NOT operator to the group.

**There are a few JQL syntax bits to get you started:**

AND --- allows you to add qualifiers to a list
!= Thing --- target one thing
is in (List, Of, Things) --- target a bunch of things (Done, Closed, Resolved) typically
not in (List, of, Things) --- do not include a bunch of things
-1w --- relative time. You can also use -1d for day
"2015/3/15" --- specific dates
