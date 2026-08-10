from mcp.server.fastmcp import FastMCP


# Clients
from tools.clients import (
    list_clients,
    create_client,
    update_client,
   
)


# Contacts
from tools.contacts import (
    list_contacts,
    create_contact,
    update_contact,
  
)


# Produits
from tools.products import (
    list_products,
    create_product,
    update_product,
  
)


# Projets
from tools.projects import (
    list_projects,
    create_project,
)


# Devis
from tools.proposals import (
    list_proposals,
    create_proposal,
    add_proposal_line,
    validate_proposal,
)


# Factures
from tools.invoices import (
    list_invoices,
    create_invoice,
    add_invoice_line,
)


# Commandes
from tools.orders import (
    list_orders,
    create_order,
)


# Catégories
from tools.categories import (
    list_categories,
    create_category,
)


# SQL
from tools.sql import (
    execute_sql,
    get_schema,
)


# Analytics
from tools.analytics import (
    get_total_clients,
    get_total_invoices,
    get_turnover,
    get_best_customers,
    get_last_clients,
    get_last_invoices,
)



mcp = FastMCP("Dolibarr MCP Server")



# ==========================
# Clients
# ==========================

mcp.tool()(list_clients)
mcp.tool()(create_client)
mcp.tool()(update_client)




# ==========================
# Contacts
# ==========================

mcp.tool()(list_contacts)
mcp.tool()(create_contact)
mcp.tool()(update_contact)




# ==========================
# Produits
# ==========================

mcp.tool()(list_products)
mcp.tool()(create_product)
mcp.tool()(update_product)




# ==========================
# Projets
# ==========================

mcp.tool()(list_projects)
mcp.tool()(create_project)



# ==========================
# Devis
# ==========================

mcp.tool()(list_proposals)
mcp.tool()(create_proposal)
mcp.tool()(add_proposal_line)
mcp.tool()(validate_proposal)



# ==========================
# Factures
# ==========================

mcp.tool()(list_invoices)
mcp.tool()(create_invoice)
mcp.tool()(add_invoice_line)



# ==========================
# Commandes
# ==========================

mcp.tool()(list_orders)
mcp.tool()(create_order)



# ==========================
# Catégories
# ==========================

mcp.tool()(list_categories)
mcp.tool()(create_category)



# ==========================
# SQL
# ==========================

mcp.tool()(execute_sql)
mcp.tool()(get_schema)



# ==========================
# Analytics
# ==========================

mcp.tool()(get_total_clients)
mcp.tool()(get_total_invoices)
mcp.tool()(get_turnover)
mcp.tool()(get_best_customers)
mcp.tool()(get_last_clients)
mcp.tool()(get_last_invoices)



if __name__ == "__main__":
    mcp.run()