from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

# Initialize FastMCP Server
mcp = FastMCP("National House Pricing")

# Dummy data for demonstration since there are no non-authenticated 
# open external APIs for real-time Chinese real estate data.
HOUSING_DATA = {
    "北京": {"price": 65000, "trend": "-2.5%"},
    "上海": {"price": 62000, "trend": "-1.8%"},
    "深圳": {"price": 58000, "trend": "-3.2%"},
    "广州": {"price": 38000, "trend": "-0.5%"},
    "杭州": {"price": 32000, "trend": "+1.2%"},
    "南京": {"price": 28000, "trend": "-1.0%"},
    "成都": {"price": 21000, "trend": "0.0%"},
    "武汉": {"price": 18000, "trend": "-0.8%"},
}

@mcp.tool()
async def get_current_price(city: str) -> str:
    """
    Get the current average house price for a specific Chinese city.
    
    Args:
        city: The name of the city in Chinese (e.g., '北京', '上海').
    """
    # Simulate an external API call with potential timeout and resilience
    try:
        async with httpx.AsyncClient() as client:
            # We hit a fast public API just to demonstrate network handling
            # In a real app, this would be the external real estate API endpoint
            await client.get("https://httpbin.org/get", timeout=2.0)
            
            if city not in HOUSING_DATA:
                return f"Error: No housing data available for city: {city}"
                
            price = HOUSING_DATA[city]["price"]
            return f"The current average house price in {city} is {price} RMB/sqm."
    except httpx.TimeoutException:
        return "Error: The external housing API timed out. Please try again later."
    except Exception as e:
        return f"Error: Failed to fetch housing data. Context: {str(e)}"

@mcp.tool()
async def get_price_trend(city: str) -> str:
    """
    Get the year-over-year (YoY) house price percentage change for a specific Chinese city.
    
    Args:
        city: The name of the city in Chinese (e.g., '北京', '上海').
    """
    # Simulate rate limiting for demonstration purposes
    if city == "TooManyRequests":
        return "Warning: You have exceeded the hourly rate limit for the API. Please back off."
        
    await asyncio.sleep(0.5) # Simulate network latency
    
    if city not in HOUSING_DATA:
        return f"Error: No housing trend data available for city: {city}"
        
    trend = HOUSING_DATA[city]["trend"]
    return f"The year-over-year house price trend in {city} is {trend}."

if __name__ == "__main__":
    # Initialize and run the server using STDIO transport (Local Mode)
    mcp.run()
